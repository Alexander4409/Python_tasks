import socket
import struct


class EGTSParser:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def disconnect(self):
        if self.sock:
            self.sock.close()
#получения пакета
    def receive_packet(self):
        header_format = '!BBHBB'
        header_size = struct.calcsize(header_format)

        header_data = self.sock.recv(header_size)
        if len(header_data) != header_size:
            return None

        version, security_key_id, packet_length, flags, service_type = struct.unpack(header_format, header_data)

        # извлечение значения из поля flags с использованием битовых операций я использовал сдвиги и маскирование
        prefix = (flags >> 6) & 0x03
        route = (flags >> 5) & 0x01
        encryption_alg = (flags >> 3) & 0x03
        compression = (flags >> 2) & 0x01
        priority = flags & 0x03

        payload_data = self.sock.recv(packet_length - header_size)
        if len(payload_data) != packet_length - header_size:
            return None

        return {
            'version': version,
            'security_key_id': security_key_id,
            'prefix': prefix,
            'route': route,
            'encryption_alg': encryption_alg,
            'compression': compression,
            'priority': priority,
            'service_type': service_type,
            'payload': payload_data
        }

    def process_record_response(self, data):
        record_number, record_status = struct.unpack('!HB', data)
        print(f"Received Record Response - Record Number: {record_number}, Status: {record_status}")

    def process_term_identity(self, data):
        term_info_format = '!HBBHBBB'
        term_id, term_type, hw_type, hw_ver, sw_ver, msg_ver, term_fw_ver = struct.unpack(term_info_format, data[:11])
        term_id_str = data[11:].decode('utf-8')
        print(f"Received Term Identity - Term ID: {term_id}, Term Type: {term_type}, Hardware Type: {hw_type} n\
                Hardware Version: {hw_ver}, Software Version: {sw_ver}, Message Version: {msg_ver} n\
                Terminal Firmware Version: {term_fw_ver}, Terminal ID String: {term_id_str}")

#lon и lat это ширина и долгота
#по скольку в протоколе указанно преобразование в микроградусы то надо разделить значение на 1800000.0
    def process_pos_data(self, data):
        lon, lat = struct.unpack('!ii', data[:8])
        lon /= 1800000.0
        lat /= 1800000.0
        print(f"Received Position Data - Latitude: {lat}, Longitude: {lon}")

    def process_ext_pos_data(self, data):
        lon, lat = struct.unpack('!ii', data[:8])
        lon /= 1800000.0
        lat /= 1800000.0
        print(f"Received Extended Position Data - Latitude: {lat}, Longitude: {lon}")


    def process_rd(self, rd_data):
        record_type, data_length = struct.unpack('!BH', rd_data[:3])
        data = rd_data[3:]

        if record_type == 0:  # EGTS_SR_RECORD_RESPONSE
            self.process_record_response(data)
        elif record_type == 1:  # EGTS_SR_TERM_IDENTITY
            self.process_term_identity(data)
        elif record_type == 16:  # EGTS_SR_POS_DATA
            self.process_pos_data(data)
        elif record_type == 17:  # EGTS_SR_EXT_POS_DATA
            self.process_ext_pos_data(data)
        # тут надо добавить обработку для конкретных типов данных и требований определенных в спецификации протокола EGTS

    def process_payload(self, payload):
        while payload:
            record_type, record_length = struct.unpack('!BH', payload[:3])
            record_data = payload[3:3 + record_length]
            self.process_rd(record_data)
            payload = payload[3 + record_length:]

    def process_packet(self, packet):
        payload = packet['payload']
        self.process_payload(payload)

        # пример отправки ответа
        response = b'ACK'
        self.sock.sendall(response)

    def run(self):
        self.connect()
        try:
            while True:
                packet = self.receive_packet()
                if packet:
                    self.process_packet(packet)
        except KeyboardInterrupt:
            pass
        finally:
            self.disconnect()


if __name__ == '__main__':
    egts_parser = EGTSParser('127.0.0.0', 12345)  # Заменить на реальный параметр
    egts_parser.run()

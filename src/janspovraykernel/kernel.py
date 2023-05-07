##!/usr/bin/env python
import os
import shutil
import pexpect
from ipykernel.kernelbase import Kernel

workingdir = "/tmp/povraykernel/"

class janspovraykernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.13.0'
    language = 'povray'
    language_version = '2.38'
    language_info = {
        'name': 'povray',
        'mimetype': 'application/povray',
        'file_extension': '.pov',
    }
    banner = "The Persistence of Vision Raytracer"


    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            if os.path.exists(workingdir):
                shutil.rmtree(workingdir)
            os.mkdir(workingdir)
            os.chdir(workingdir)
            with open("code.pov", "w") as f:
                    f.write(code)
            solution = pexpect.run(f'povray +UA -d {workingdir}code.pov').decode('ascii')
            if os.path.exists(f'{workingdir}code.png'):
                with open(f'{workingdir}code.png', "rb") as file:
                        solution = file.read()
                stream_content = {'metadata': {}, 'data': {'image/png': solution}}
                self.send_response(self.iopub_socket, 'display_data', stream_content)
            else:
                stream_content = {'name': 'stdout', 'text': solution}
                self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

        def do_shutdown(self, restart):
            if os.path.exists(workingdir):
                shutil.rmtree(workingdir)

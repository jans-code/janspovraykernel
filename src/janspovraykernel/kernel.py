##!/usr/bin/env python
import os
import shutil
import pexpect
from ipykernel.kernelbase import Kernel

commands = ['aa_level', 'aa_threshold', 'abs', 'absorption', 'accuracy', 'acos', 'acosh', 'adaptive', 'adc_bailout',
            'agate', 'agate_turb', 'all', 'all_intersections', 'alpha', 'altitude', 'always_sample', 'ambient',
            'ambient_light', 'angle', 'aperture', 'append', 'arc_angle', 'area_light', 'array', 'asc', 'ascii',
            'asin', 'asinh', 'assumed_gamma', 'atan', 'atan2', 'atanh', 'autostop', 'average', 'b_spline',
            'background', 'bezier_spline', 'bicubic_patch', 'black_hole', 'blob', 'blue', 'blur_samples',
            'bounded_by', 'box', 'boxed', 'bozo', 'break', 'brick', 'brick_size', 'brightness', 'brilliance',
            'bump_map', 'bump_size', 'bumps', 'camera', 'case', 'caustics', 'ceil', 'cells', 'charset', 'checker',
            'chr', 'circular', 'clipped_by', 'clock', 'clock_delta', 'clock_on', 'collect', 'color', 'color_map',
            'colour', 'colour_map', 'component', 'composite', 'concat', 'cone', 'confidence', 'conic_sweep',
            'conserve_energy', 'contained_by', 'control0', 'control1', 'coords', 'cos', 'cosh', 'count', 'crackle',
            'crand', 'cube', 'cubic', 'cubic_spline', 'cubic_wave', 'cutaway_textures', 'cylinder', 'cylindrical',
            'debug', 'declare', 'default', 'defined', 'degrees', 'density', 'density_file', 'density_map', 'dents',
            'df3', 'difference', 'diffuse', 'dimension_size', 'dimensions', 'direction', 'disc', 'dispersion',
            'dispersion_samples', 'dist_exp', 'distance', 'div', 'double_illuminate', 'eccentricity', 'else',
            'emission', 'end', 'error', 'error_bound', 'evaluate', 'exp', 'expand_thresholds', 'exponent',
            'exterior', 'extinction', 'face_indices', 'facets', 'fade_color', 'fade_colour', 'fade_distance',
            'fade_power', 'falloff', 'falloff_angle', 'false', 'fclose', 'file_exists', 'filter', 'final_clock',
            'final_frame', 'finish', 'fisheye', 'flatness', 'flip', 'floor', 'focal_point', 'fog', 'fog_alt',
            'fog_offset', 'fog_type', 'fopen', 'form', 'frame_number', 'frequency', 'fresnel', 'function',
            'gather', 'gif', 'global_lights', 'global_settings', 'gradient', 'granite', 'gray', 'gray_threshold',
            'green', 'height_field', 'hexagon', 'hf_gray_16', 'hierarchy', 'hypercomplex', 'hollow', 'if', 'ifdef',
            'iff', 'ifndef', 'image_height', 'image_map', 'image_pattern', 'image_width', 'include',
            'initial_clock', 'initial_frame', 'inside', 'inside_vector', 'int', 'interior', 'interior_texture',
            'internal', 'interpolate', 'intersection', 'intervals', 'inverse', 'ior', 'irid', 'irid_wavelength',
            'isosurface', 'jitter', 'jpeg', 'julia', 'julia_fractal', 'lambda', 'lathe', 'leopard', 'light_group',
            'light_source', 'linear_spline', 'linear_sweep', 'ln', 'load_file', 'local', 'location', 'log',
            'look_at', 'looks_like', 'low_error_factor', 'macro', 'magnet', 'major_radius', 'mandel', 'map_type',
            'marble', 'material', 'material_map', 'matrix', 'max', 'max_extent', 'max_gradient',
            'max_intersections', 'max_iteration', 'max_sample', 'max_trace', 'max_trace_level', 'media',
            'media_attenuation', 'media_interaction', 'merge', 'mesh', 'mesh2', 'metallic', 'method', 'metric',
            'min', 'min_extent', 'minimum_reuse', 'mod', 'mortar', 'natural_spline', 'nearest_count', 'no',
            'no_bump_scale', 'no_image', 'no_reflection', 'no_shadow', 'noise_generator', 'normal',
            'normal_indices', 'normal_map', 'normal_vectors', 'number_of_waves', 'object', 'octaves', 'off',
            'offset', 'omega', 'omnimax', 'on', 'once', 'onion', 'open', 'orient', 'orientation', 'orthographic',
            'panoramic', 'parallel', 'parametric', 'pass_through', 'pattern', 'perspective', 'pgm', 'phase',
            'phong', 'phong_size', 'photons', 'pi', 'pigment', 'pigment_map', 'pigment_pattern', 'planar', 'plane',
            'png', 'point_at', 'poly', 'poly_wave', 'polygon', 'pot', 'pow', 'ppm', 'precision', 'precompute',
            'pretrace_end', 'pretrace_start', 'prism', 'prod', 'projected_through', 'pwr', 'quadratic_spline',
            'quadric', 'quartic', 'quaternion', 'quick_color', 'quick_colour', 'quilted', 'radial', 'radians',
            'radiosity', 'radius', 'rainbow', 'ramp_wave', 'rand', 'range', 'ratio', 'read', 'reciprocal',
            'recursion_limit', 'red', 'reflection', 'reflection_exponent', 'refraction', 'render', 'repeat', 'rgb',
            'rgbf', 'rgbft', 'rgbt', 'right', 'ripples', 'rotate', 'roughness', 'samples', 'save_file', 'scale',
            'scallop_wave', 'scattering', 'seed', 'select', 'shadowless', 'sin', 'sine_wave', 'sinh', 'size',
            'sky', 'sky_sphere', 'slice', 'slope', 'slope_map', 'smooth', 'smooth_triangle', 'solid', 'sor',
            'spacing', 'specular', 'sphere', 'sphere_sweep', 'spherical', 'spiral1', 'spiral2', 'spline',
            'split_union', 'spotlight', 'spotted', 'sqr', 'sqrt', 'statistics', 'str', 'strcmp', 'strength',
            'strlen', 'strlwr', 'strupr', 'sturm', 'substr', 'sum', 'superellipsoid', 'switch', 'sys', 't', 'tan',
            'tanh', 'target', 'text', 'texture', 'texture_list', 'texture_map', 'tga', 'thickness', 'threshold',
            'tiff', 'tightness', 'tile2', 'tiles', 'tolerance', 'toroidal', 'torus', 'trace', 'transform',
            'translate', 'transmit', 'triangle', 'triangle_wave', 'true', 'ttf', 'turb_depth', 'turbulence',
            'type', 'u', 'u_steps', 'ultra_wide_angle', 'undef', 'union', 'up', 'use_alpha', 'use_color',
            'use_colour', 'use_index', 'utf8', 'uv_indices', 'uv_mapping', 'uv_vectors', 'v', 'v_steps', 'val',
            'variance', 'vaxis_rotate', 'vcross', 'vdot', 'version', 'vertex_vectors', 'vlength', 'vnormalize',
            'vrotate', 'vstr', 'vturbulence', 'warning', 'warp', 'water_level', 'waves', 'while', 'width', 'wood',
            'wrinkles', 'write', 'x', 'y', 'yes', 'All reserved keywords', 'z']

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

    def do_complete(self, code, cursor_pos):
        
        if " " in code:
            cursor_pos = code.rfind(" ") + 1
        else:
            cursor_pos = 0
        
        options = []
        for command in commands:
            if command.startswith(code.split(" ")[-1].lower()):
                options.append(command)

        return {
            'matches': options,
            'metadata': {},
            'status': 'ok',
            'cursor_start': cursor_pos,
            'cursor_end': len(code)
        }
    
    def do_shutdown(self, restart):
        if os.path.exists(workingdir):
            shutil.rmtree(workingdir)

import os

ABSOLUTE_PATH = ''
RESULT_FOLDER = 'images/filtered_images'
SAVE_PATH = os.path.realpath(RESULT_FOLDER) + '/{}'
checkpoint_path = 'checkpoint' # name of your checkpoint folder
algorithm_script_name = '{}/evaluate.py'.format(ABSOLUTE_PATH) 
shell_script = 'python {} --checkpoint {} --in-path {}  --out-path {} --device gpu:0'


ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_image(image_filename):
    image_path = os.path.realpath(image_filename)
    algorithm_checkpoint_path = '{}/{}'.format(ABSOLUTE_PATH, checkpoint_path)
    new_image_filename = image_filename.split('/')[1] # /images
    name = os.path.splitext(new_image_filename)[0] 
    ext = os.path.splitext(new_image_filename)[1] 
    new_filename = name + '_stylish' + ext
    final_command = shell_script.format(algorithm_script_name, algorithm_checkpoint_path, image_path, SAVE_PATH.format(new_filename))
    if os.system(final_command) == 0:
        link = '{}/{}'.format(RESULT_FOLDER, new_filename)
        return link
    else:
        return 'Error in shell script or syntax!'    
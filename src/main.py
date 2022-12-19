import os

DICOM_DIR = '/mnt/localscratch/cds/rbrecheisen/raw/tlodewick-ct-noise-1/AL_100%/101816478/2-Abdomen'
TMP_DIR = '/mnt/localscratch/cds/rbrecheisen/processed/tlodewick-ct-noise-1-out-1'
DCM2NII = '/usr/bin/dcm2niix'

def dcm2nii():
    if not os.path.isfile(os.path.join(TMP_DIR, 'my_file.nii.gz')):
        os.system(f'{DCM2NII} -m y -z y -f my_file -o {TMP_DIR} {DICOM_DIR}')
    else:
        print('dcm2nii() output already exists')

def nii2seg():
    pass

def main():
    dcm2nii()
    nii2seg()


if __name__ == '__main__':
    main()

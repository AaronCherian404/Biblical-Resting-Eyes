import os
import shutil
import sys
import PyInstaller.__main__

def clean_directories():
    """Clean up build directories"""
    directories = ['build', 'dist', '__pycache__']
    for directory in directories:
        if os.path.exists(directory):
            shutil.rmtree(directory)
    if os.path.exists('BibleBreak.spec'):
        os.remove('BibleBreak.spec')

def build_executable():
    """Build the executable using PyInstaller"""
    try:
        PyInstaller.__main__.run([
            'bible_break.py',
            '--name=BibleBreak',
            '--onefile',
            '--noconsole',
            '--clean'
        ])
        print("Build completed successfully!")
        print(f"Executable can be found in the 'dist' folder")
    except Exception as e:
        print(f"Error during build: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    print("Starting build process...")
    print("Cleaning up previous builds...")
    clean_directories()
    print("Building executable...")
    build_executable()
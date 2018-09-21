import os
def MostRecentAudioClip():
    max_mtime = 0
    for dirname,subdirs,files in os.walk("Audio/."):
        for fname in files:
            full_path = os.path.join(dirname, fname)
            mtime = os.stat(full_path).st_mtime
            if mtime > max_mtime:
                max_mtime = mtime
                max_dir = dirname
                max_file = fname

    return max_file
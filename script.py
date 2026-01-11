import requests
import zipfile
import tempfile
import shutil
import os
import hashlib

WORKER_BASE = "https://mod-artifact-proxy.waleedarshad7353.workers.dev"
META_URL = f"{WORKER_BASE}/meta"
DOWNLOAD_URL = WORKER_BASE

MODS_FOLDER = r"your mods folder path here"
SHA_FILE = os.path.join(MODS_FOLDER, "devonian.sha")


def get_remote_meta():
    r = requests.get(META_URL, timeout=5)
    r.raise_for_status()
    return r.json()


def get_local_sha():
    if os.path.exists(SHA_FILE):
        with open(SHA_FILE, "r") as f:
            return f.read().strip()
    return None


def save_local_sha(sha):
    with open(SHA_FILE, "w") as f:
        f.write(sha)


def download_and_extract(url, tmp_dir):
    zip_path = os.path.join(tmp_dir, "artifact.zip")

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(zip_path, "wb") as f:
            shutil.copyfileobj(r.raw, f)

    with zipfile.ZipFile(zip_path) as z:
        z.extractall(tmp_dir)

    jar_files = [
        f for f in os.listdir(tmp_dir)
        if f.endswith(".jar") and "sources" not in f.lower()
    ]

    if not jar_files:
        raise RuntimeError("No mod JAR found in artifact")

    return jar_files[0]


def install_mod(tmp_dir, jar_name):
    source_path = os.path.join(tmp_dir, jar_name)
    target_path = os.path.join(MODS_FOLDER, jar_name)

    if os.path.exists(target_path):
        os.replace(target_path, target_path + ".bak")

    shutil.move(source_path, target_path)
    print(f"{jar_name} installed successfully!")


def main():
    print("Checking for Devonian updates...")

    meta = get_remote_meta()
    remote_sha = meta["sha"]

    local_sha = get_local_sha()

    print("Remote SHA:", remote_sha)
    print("Local SHA:", local_sha or "none")

    if local_sha == remote_sha:
        print("Mod already up to date. Skipping download.")
        return

    print("Downloading latest Devonian build…")
    print("GitHub run:", meta["html_url"])

    with tempfile.TemporaryDirectory() as tmp:
        jar_name = download_and_extract(DOWNLOAD_URL, tmp)
        install_mod(tmp, jar_name)

    save_local_sha(remote_sha)
    print("Devonian update complete!")


if __name__ == "__main__":
    main()

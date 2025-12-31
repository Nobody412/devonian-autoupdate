import requests
import zipfile
import tempfile
import shutil
import os

RUN_ID = "run.id"

WORKER_URL = f"https://mod-artifact-proxy.waleedarshad7353.workers.dev/?run_id={RUN_ID}"
MODS_FOLDER = r"mincraft folder path here"

def fetch_headers(url):
    try:
        r = requests.head(url, allow_redirects=True)
        r.raise_for_status()
        headers = {
            "X-Source-URL": r.headers.get("X-Source-URL"),
            "X-GitHub-Run": r.headers.get("X-GitHub-Run")
        }
        return headers
    except Exception as e:
        print("Failed to fetch headers:", e)
        return {}

def download_and_extract(url, tmp_dir):
    zip_path = os.path.join(tmp_dir, "artifact.zip")
    r = requests.get(url, stream=True)
    r.raise_for_status()

    with open(zip_path, "wb") as f:
        shutil.copyfileobj(r.raw, f)

    with zipfile.ZipFile(zip_path) as z:
        z.extractall(tmp_dir)

    jar_files = [f for f in os.listdir(tmp_dir) if f.endswith(".jar") and "sources" not in f.lower()]
    if not jar_files:
        raise RuntimeError("No mod JAR found in artifact")

    return jar_files[0]

def install_mod(tmp_dir, jar_name):
    target_path = os.path.join(MODS_FOLDER, jar_name)
    source_path = os.path.join(tmp_dir, jar_name)

    if os.path.exists(target_path):
        os.replace(target_path, target_path + ".bak")

    shutil.move(source_path, target_path)
    print(f"{jar_name} installed successfully!")

def main():
    print("Downloading latest Devonian build...")
    print("Via worker:", WORKER_URL)

    headers = fetch_headers(WORKER_URL)
    if headers:
        print("Verification headers:")
        for k, v in headers.items():
            print(f"{k}: {v}")

    with tempfile.TemporaryDirectory() as tmp:
        jar_name = download_and_extract(WORKER_URL, tmp)
        install_mod(tmp, jar_name)

    print("Devonian update complete!")

if __name__ == "__main__":
    main()

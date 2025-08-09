import os
import subprocess

def run_command(command, cwd):
    result = subprocess.run(command, cwd=cwd, shell=True, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def remote_exists(remote_name, cwd):
    code, out, err = run_command("git remote", cwd)
    return remote_name in out.splitlines()

def main():
    # Set base directory explicitly
    base_dir = r"C:\Users\rahmanim\repos"

    for entry in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, entry)

        if os.path.isdir(folder_path) and os.path.isdir(os.path.join(folder_path, ".git")):
            print("\n" + "=" * 60)
            print(f"📁 REPOSITORY: {entry}")
            print("=" * 60)

            choice = input("    → Press [Enter] to continue, 's' to skip, or storage a custom commit message: ").strip()
            if choice.lower() == 's':
                print("    → Skipped.")
                continue

            commit_msg = choice if choice else input("    → Enter commit message: ").strip()

            print("  → git add .")
            run_command("git add .", folder_path)

            print(f'  → git commit -m "{commit_msg}"')
            run_command(f'git commit -m "{commit_msg}"', folder_path)

            if remote_exists("mghub", folder_path):
                print("  → git push mghub main")
                run_command("git push mghub main", folder_path)
            else:
                print("  → Skipping mghub (remote not found)")

            print("  → git push unigraz main")
            run_command("git push unigraz main", folder_path)

if __name__ == "__main__":
    main()

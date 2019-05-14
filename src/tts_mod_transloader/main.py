"""
The entry point to the TTS Mod Transloader program.
"""


def main():
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive
    import os

    g_login = GoogleAuth()
    g_login.LocalWebserverAuth()
    drive = GoogleDrive(g_login)


if __name__ == "__main__":
    main()

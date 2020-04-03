# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['table.py'],
             pathex=['C:\\Users\\Caio\\Documents\\ProgramaLoja\\Pcompile'],
             binaries=[('bdconnect.py', '.'), ('adduser.py', '.')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=True,
             win_private_assemblies=True,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='table',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )

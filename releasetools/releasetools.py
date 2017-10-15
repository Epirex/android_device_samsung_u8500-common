def FullOTA_InstallEnd(info):
	info.script.AppendExtra('symlink("/system/lib/libjhead.so", "/system/lib/libhead.so");')
	info.script.AppendExtra('run_program("/sbin/make_ext4fs", "/dev/block/mmcblk0p9");')

# Symlink some dependencies of libcscall.so
	info.script.AppendExtra('symlink("/system/lib/ste_omxcomponents/libste_dec_amr.so", "/system/lib/libste_dec_amr.so");')
	info.script.AppendExtra('symlink("/system/lib/ste_omxcomponents/libste_enc_amr.so", "/system/lib/libste_enc_amr.so");')
	info.script.AppendExtra('symlink("/system/lib/ste_omxcomponents/libste_dec_amrwb.so", "/system/lib/libste_dec_amrwb.so");')
info.script.AppendExtra('symlink("/system/lib/ste_omxcomponents/libste_enc_amrwb.so", "/system/lib/libste_enc_amrwb.so");')

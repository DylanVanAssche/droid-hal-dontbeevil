#These and other macros are documented in dhd/droid-hal-device.inc
%define device onyx
%define vendor oneplus
%define vendor_pretty OnePlus
%define device_pretty X
%define installable_zip 1
%define enable_kernel_update 1

%define android_config \
#define DROID_AUDIO_HAL_ATOI_FIX 1\
%{nil}

%define straggler_files\
    /selinux_version\
    /service_contexts\
%{nil}
%include rpm/dhd/droid-hal-device.inc

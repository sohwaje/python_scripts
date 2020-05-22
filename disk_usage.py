import sys, os, psutil
from psutil._common import bytes2human
"""
# Windows
Device               Total     Used     Free  Use %      Type  Mount
C:\                 238.4G   155.7G    82.6G    65%      NTFS  C:\
E:\                   1.8T   279.6G     1.5T    15%      NTFS  E:\

# Linux
Device               Total     Used     Free  Use %      Type  Mount
/dev/sda2            29.5G     3.4G    26.1G    11%       xfs  /
/dev/sda1           496.7M    64.0M   432.7M    12%       xfs  /boot
/dev/sdb1            15.6G    44.0M    14.8G     0%      ext4  /mnt/resource

# part를 출력하면 다음과 같다.
sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed')
sdiskpart(device='D:\\', mountpoint='D:\\', fstype='', opts='cdrom')
sdiskpart(device='E:\\', mountpoint='E:\\', fstype='NTFS', opts='rw,fixed')

# usage를 출력하면 아래와 같다.
sdiskusage(total=255953203200, used=167104131072, free=88849072128, percent=65.3)
sdiskusage(total=2000396742656, used=300253265920, free=1700143476736, percent=15.0)
"""
def main():
    templ = "%-17s %8s %8s %8s %5s%% %9s  %s" # 출력할 문자열 위치를 변수 templ에 담는다.
    print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type", "Mount"))

    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt': # os가 nt 계열일 경우 참, 리눅스는 posix
            if 'cdrom' in part.opts or part.fstype =='': # opts가 'cdrom'이거나, fstype이 비어 있을 경우에 참.
            # 디스크가 없는 CD-ROM일 경우 윈도우즈는 GUI error를 일으키거나 멈출 수 있기 때문에 건너뛴다.
                continue
        usage = psutil.disk_usage(part.mountpoint) # 아래와 같이 튜플 형식으로 디스크 사용량을 나타낸다.
        print(templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint))

if __name__ == '__main__':
    sys.exit(main())




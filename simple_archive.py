import datetime
import os
import zipfile


def gather_old_directories(directory, today):
    directories = []
    directories_old = []

    for root, dirs, files in os.walk(directory):
        if len(dirs) == 0:
            directories.append(root)

    for d in directories:
        dates = d.split("\\")
        folder_date = datetime.datetime(int(dates[2]), int(dates[3]), int(dates[4]))
        diff = today - folder_date
        if diff.days > 90:
            directories_old.append(d)

    return directories_old


def archive_directories(directories_list, today):
    filename = 'D:\\NFS_storage\\' + '-'.join(today.strftime("%x").split('/')) + "'s launch archive" + '.zip'
    dir_archive = zipfile.ZipFile(filename, mode='a')
    for name in directories_list:
        dir_archive.write(name)
    dir_archive.close()


def migrate(directory):
    current_date = datetime.datetime.now()
    to_be_archived = gather_old_directories(directory, current_date)
    archive_directories(to_be_archived, current_date)

    with open('log.txt', 'a') as L:
        L.write('Archived data for past {} days on {}'.format(len(to_be_archived),
                                                              current_date.strftime("%c")))


migrate(r'D:\z')

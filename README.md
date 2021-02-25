# simple_archive

Функция gather_old_directories() составляет список всех папок, которые нужно архивировать (это папки старше 90 дней)

Функция archive_directories() создаёт архив в папке NFS_storage (которая должна существовать до архивации)

Функция migrate() использует gather_old_directories() и archive_directories() для архивации и добавляет запись в log.txt

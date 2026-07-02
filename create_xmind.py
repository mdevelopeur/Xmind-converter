import xmind

# 1. Создаем рабочую книгу (Workbook)
workbook = xmind.load("my_first_mindmap.xmind")

# 2. Получаем первый лист (Sheet) или создаем новый
sheet = workbook.get_first_sheet()
sheet.setTitle("Главный проект")

# 3. Устанавливаем корневую тему
root_topic = sheet.get_root_topic()
root_topic.setTitle("Разработка на Python")

# 4. Добавляем подтемы (узлы 1-го уровня)
topic1 = root_topic.add_subtopic()
topic1.setTitle("Бэкенд")

topic2 = root_topic.add_subtopic()
topic2.setTitle("Фронтенд")

# 5. Добавляем вложенные темы (узлы 2-го уровня)
sub_topic1 = topic1.add_subtopic()
sub_topic1.setTitle("Django")

sub_topic2 = topic1.add_subtopic()
sub_topic2.setTitle("FastAPI")

# 6. Сохраняем карту в файл
xmind.save(workbook, "my_first_mindmap.xmind")

# Как изменить руководство

## Предложение

Создайте Issue с проблемой, примером текста и ожидаемым результатом.
Для небольшой правки можно сразу открыть Pull Request с таким описанием.
Не загружайте персональные записи или тексты общения.

## Локальный запуск

Требуются Python 3.12 и Git. Выполните команды из корня репозитория.

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m pymarkdown --config .pymarkdown.json scan docs
.venv\Scripts\python.exe scripts/check_style.py
.venv\Scripts\python.exe -m mkdocs build --strict
.venv\Scripts\python.exe -m mkdocs serve
```

Откройте адрес из консоли. Для завершения сервера нажмите Ctrl+C.

## Ветка и коммит

Создайте ветку от актуальной main: `git switch -c docs/topic`.
Формат сообщения: `type: краткое описание`.
Используйте `docs` для текста, `ci` для workflow и `fix` для исправления ошибки.
Пример: `docs: add accessibility rules`.

## Новый раздел

Создайте файл в docs с одним заголовком первого уровня.
Добавьте путь в nav файла mkdocs.yml. Проверьте ссылки, линтер и сборку.
Включите файл и изменение навигации в один коммит.

## Ревью

Откройте PR в main, опишите задачу и проверки. Пригласите другого студента.
Рецензент проверяет терминологию, структуру, применимость правил и примеры.
Замечание содержит место, проблему и предложенное исправление либо вопрос.
Автор отвечает по существу, исправляет текст и отправляет повторный коммит.
После одобрения и успешного CI владелец выполняет merge.
Откройте Actions и проверьте deploy, затем опубликованную страницу.

## Источники

- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
- [Документация MkDocs](https://www.mkdocs.org/).

# Конвертер цветов эффектов для игры Ex Machina

## Использование

1) Распаковать в папку.
2) В папке зажать Shift и ПКМ. В контекстном меню выбрать "Открыть в терминале" (Либо используем любой другой терминал на своё )
3) Пишем .\colorconverter.exe --help и получаем все команды. Следуем инструкциям.

## Примеры

Конвертация из RGBA в DEC

```sh
.\main.exe -mode rgba_to_dec -r 0 -g 0 -b 0 -a 255
```

Конвертация из DEC в RGBA

```sh
.\main.exe -mode dec_to_rgba -color -16777216
```

==================================================

Создано для сообщества: DeusExMachina
Автор: OverLine

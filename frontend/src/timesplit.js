export function getMinutesSince(dateString) {
    // Парсим дату из строки
    const pastDate = new Date(dateString);

    // Получаем текущее время в формате UTC
    const currentTime = new Date().toUTCString();

    // Получаем дату прошлого события в формате UTC
    const pastTime = pastDate.toUTCString();

    console.log(currentTime,pastTime)
    // Получаем разницу в миллисекундах между текущим временем и временем прошлого события
    let differenceInMilliseconds = new Date(currentTime).getTime() - new Date(pastTime).getTime();

    // Преобразуем разницу в минуты
    let differenceInMinutes = Math.floor(differenceInMilliseconds / (1000 * 60));

    // Если разница больше 240 минут, возвращаем 240
    if (differenceInMinutes > 240) {
        return 240;
    }

    // Иначе возвращаем фактическое количество минут
    return differenceInMinutes;
}
// calculate.js

// Функция для вычисления общего дохода от комнат
export function calculateTotalIncome(roomsData) {
    let totalIncome = 0;

    for (let room of roomsData) {
        let roomIncome = 0;

        // Вычисляем доход от каждого устройства комнаты
        let compIncome = calculateIncomeFromDevice(room.comp_lvl, room.lvl);
        let webcamIncome = calculateIncomeFromDevice(room.webcam_lvl, room.lvl);
        let microIncome = calculateIncomeFromDevice(room.micro_lvl, room.lvl);

        // Добавляем доход от каждого устройства к общему доходу комнаты
        roomIncome = compIncome + webcamIncome + microIncome;

        // Добавляем доход от всех устройств комнаты к общему доходу
        totalIncome += roomIncome;
    }

    return totalIncome;
}

// Функция для вычисления дохода от устройства в комнате
function calculateIncomeFromDevice(deviceLevel, roomLevel) {
    const incomeTable = {
        1: [0, 180, 370, 570, 850],
        2: [0, 360, 760, 1260, 2000],
        3: [0, 960, 1960, 3160, 4500],
        4: [0, 1500, 3500, 6000, 10000],
        5: [0, 3000, 6500, 10500, 16500]
    };

    return incomeTable[roomLevel][deviceLevel - 1];
}

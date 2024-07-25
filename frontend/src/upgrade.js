export function getUpgradePrices(data) {
    const roomLevel = data.lvl;
    const compLevel = data.comp_lvl;
    const webcamLevel = data.webcam_lvl;
    const microLevel = data.micro_lvl;
    const upgradePrices = {};

    // Таблицы цен для улучшения, текущего прироста дохода и прироста за уровень для каждого устройства в комнате
    const upgradePriceTable = {
        1: {
            comp: { up: [1500, 2500, 5000, 8000], cur: [0, 180, 370, 570, 850], inc: [180, 190, 200, 280, 280] },
            webcam: { up: [1500, 2500, 5000, 8000], cur: [0, 180, 370, 570, 850], inc: [180, 190, 200, 280, 280] },
            micro: { up: [1500, 2500, 5000, 8000], cur: [0, 180, 370, 570, 850], inc: [180, 190, 200, 280, 280] }
        },
        2: {
            comp: { up: [3000, 5000, 10000, 16000], cur: [0, 360, 760, 1260, 2000], inc: [360, 400, 500, 740, 740] },
            webcam: { up: [3000, 5000, 10000, 16000], cur: [0, 360, 760, 1260, 2000], inc: [360, 400, 500, 740, 740] },
            micro: { up: [3000, 5000, 10000, 16000], cur: [0, 360, 760, 1260, 2000], inc: [360, 400, 500, 740, 740] }
        },
        3: {
            comp: { up: [7500, 12500, 20000, 25000], cur: [0, 960, 1960, 3160, 4500], inc: [960, 1000, 1100, 1340, 1340] },
            webcam: { up: [7500, 12500, 20000, 25000], cur: [0, 960, 1960, 3160, 4500], inc: [960, 1000, 1100, 1340, 1340] },
            micro: { up: [7500, 12500, 20000, 25000], cur: [0, 960, 1960, 3160, 4500], inc: [960, 1000, 1100, 1340, 1340] }
        },
        4: {
            comp: { up: [30000, 35000, 41250, 58750], cur: [0, 1500, 3500, 6000, 10000], inc: [1500, 2000, 2500, 4000, 4000] },
            webcam: { up: [30000, 35000, 41250, 58750], cur: [0, 1500, 3500, 6000, 10000], inc: [1500, 2000, 2500, 4000, 4000] },
            micro: { up: [30000, 35000, 41250, 58750], cur: [0, 1500, 3500, 6000, 10000], inc: [1500, 2000, 2500, 4000, 4000] }
        },
        5: {
            comp: { up: [60000, 70000, 87500, 132500], cur: [0, 3000, 6500, 10500, 16500], inc: [3000, 3500, 4000, 6000, 6000] },
            webcam: { up: [60000, 70000, 87500, 132500], cur: [0, 3000, 6500, 10500, 16500], inc: [3000, 3500, 4000, 6000, 6000] },
            micro: { up: [60000, 70000, 87500, 132500], cur: [0, 3000, 6500, 10500, 16500], inc: [3000, 3500, 4000, 6000, 6000] }
        }
    };

    // Получаем цены на улучшение, текущий прирост дохода и прирост за уровень для каждого устройства в соответствии с переданными уровнями устройств
    upgradePrices.comp_up = upgradePriceTable[roomLevel].comp.up[compLevel - 1];
    upgradePrices.webcam_up = upgradePriceTable[roomLevel].webcam.up[webcamLevel - 1];
    upgradePrices.micro_up = upgradePriceTable[roomLevel].micro.up[microLevel - 1];

    upgradePrices.comp_cur = upgradePriceTable[roomLevel].comp.cur[compLevel-1];
    upgradePrices.webcam_cur = upgradePriceTable[roomLevel].webcam.cur[webcamLevel-1];
    upgradePrices.micro_cur = upgradePriceTable[roomLevel].micro.cur[microLevel-1];

    upgradePrices.comp_inc = upgradePriceTable[roomLevel].comp.inc[compLevel-1];
    upgradePrices.webcam_inc = upgradePriceTable[roomLevel].webcam.inc[webcamLevel-1];
    upgradePrices.micro_inc = upgradePriceTable[roomLevel].micro.inc[microLevel-1];

    return upgradePrices;
}
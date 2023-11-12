
<template>
    <div style="width: 100%; height: 100%; position: relative; background: #F60C0C">
    <div style="width: 100%; height: 135px; left: 0px; top: 0px; position: absolute; background: #053B50"></div>
    <div style="width: 360px; height: 811px; left: 920px; top: 184px; position: absolute; background: #176B87; border-radius: 15px"></div>
    <div style="width: 645px; height: 689px; left: 160px; top: 306px; position: absolute; background: #176B87; border-radius: 15px"></div>
    <div style="width: 486px; height: 101px; left: 477px; top: 17px; position: absolute; text-align: center; color: #EEEEEE; font-size: 70px; font-family: Kanit; font-weight: 600; line-height: 90px; word-wrap: break-word">Parking ++</div>
    <div style="width: 595px; padding-left: 8px; padding-right: 8px; left: 185px; top: 221px; position: absolute; background: white; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.16); border-radius: 24px; overflow: hidden; justify-content: flex-start; align-items: flex-start; gap: 8px; display: inline-flex">
        <img style="width: 40px; height: 40px" src="https://via.placeholder.com/40x40" />
        <div style="width: 225px; height: 40px; opacity: 0.30; color: black; font-size: 30px; font-family: Inter; font-weight: 400; word-wrap: break-word"><br/><br/><br/>Enter Location</div>
    </div>
    <div style="width: 302px; height: 6px; left: 945px; top: 418px; position: absolute; background: #EEEEEE; border-radius: 100px"></div>
    <div style="height: 436px; left: 952px; top: 488px; position: absolute; flex-direction: column; justify-content: flex-start; align-items: flex-start; gap: 55px; display: inline-flex">
        <div style="width: 288px; text-align: center; color: white; font-size: 32px; font-family: Kanit; font-weight: 600; line-height: 40px; word-wrap: break-word">Selected Parking:</div>
        <div style="justify-content: flex-start; align-items: center; gap: 15px; display: inline-flex">
            <div style="width: 53px; flex-direction: column; justify-content: flex-start; align-items: flex-end; gap: 55px; display: inline-flex">
                <div style="width: 45px; height: 45px; position: relative">
                    <div style="width: 33.75px; height: 41.25px; left: 5.62px; top: 1.88px; position: absolute; border: 2px #EEEEEE solid"></div>
                    <div style="width: 11.25px; height: 11.25px; left: 16.88px; top: 13.12px; position: absolute; border: 2px #EEEEEE solid"></div>
                </div>
                <div style="width: 45px; height: 45px; position: relative; background: #176B87">
                    <div style="width: 0px; height: 41.25px; left: 22.50px; top: 1.88px; position: absolute; border: 2px #EEEEEE solid"></div>
                    <div style="width: 22.50px; height: 26.25px; left: 11.25px; top: 9.38px; position: absolute; border: 2px #EEEEEE solid"></div>
                </div>
                <div style="width: 45px; height: 45px; position: relative">
                    <div style="width: 37.50px; height: 37.50px; left: 3.75px; top: 3.75px; position: absolute; border: 2px #EEEEEE solid"></div>
                    <div style="width: 7.50px; height: 15px; left: 22.50px; top: 11.25px; position: absolute; border: 2px #EEEEEE solid"></div>
                </div>
            </div>
            <div style="height: 241px; flex-direction: column; justify-content: flex-start; align-items: flex-start; gap: 60px; display: inline-flex">
                <div style="text-align: center; color: #EEEEEE; font-size: 32px; font-family: Kanit; font-weight: 600; line-height: 40px; word-wrap: break-word">Mi Away</div>
                <div style="text-align: center; color: #EEEEEE; font-size: 32px; font-family: Kanit; font-weight: 600; line-height: 40px; word-wrap: break-word">$/hour</div>
                <div style="text-align: center; color: white; font-size: 32px; font-family: Kanit; font-weight: 600; line-height: 40px; word-wrap: break-word">Available till</div>
            </div>
        </div>
        <div style="width: 288px; height: 41px; text-align: center; color: white; font-size: 20px; font-family: Kanit; font-weight: 400; line-height: 20px; word-wrap: break-word">Reference the street view to gauge parking space size</div>
    </div>
    <div style="left: 920px; top: 215px; position: absolute; flex-direction: column; justify-content: flex-start; align-items: center; gap: 28px; display: inline-flex">
        <div style="height: 80px; flex-direction: column; justify-content: flex-start; align-items: center; gap: 20px; display: flex">
            <div style="width: 345px; text-align: center; color: #EEEEEE; font-size: 32px; font-family: Kanit; font-weight: 600; line-height: 40px; word-wrap: break-word">Max Miles from Destination</div>
        </div>
        <div style="justify-content: flex-start; align-items: flex-start; gap: 20px; display: inline-flex">
            <div style="width: 67px; height: 48px; padding: 10px; background: #64CCC5; border-radius: 15px; justify-content: center; align-items: center; gap: 10px; display: flex">
                <div style="text-align: center; color: #EEEEEE; font-size: 20px; font-family: Kanit; font-weight: 400; line-height: 20px; word-wrap: break-word">0.2</div>
            </div>
            <div style="width: 67px; height: 48px; padding: 10px; background: #64CCC5; border-radius: 15px; justify-content: center; align-items: center; gap: 10px; display: flex">
                <div style="text-align: center; color: #EEEEEE; font-size: 20px; font-family: Kanit; font-weight: 400; line-height: 20px; word-wrap: break-word">0.5</div>
            </div>
            <div style="width: 67px; height: 48px; padding: 10px; background: #64CCC5; border-radius: 15px; justify-content: center; align-items: center; gap: 10px; display: flex">
                <div style="text-align: center; color: #EEEEEE; font-size: 20px; font-family: Kanit; font-weight: 400; line-height: 20px; word-wrap: break-word">0.7</div>
            </div>
            <div style="width: 67px; height: 48px; padding: 10px; background: #64CCC5; border-radius: 15px; justify-content: center; align-items: center; gap: 10px; display: flex">
                <div style="text-align: center; color: #EEEEEE; font-size: 20px; font-family: Kanit; font-weight: 400; line-height: 20px; word-wrap: break-word">1.0</div>
            </div>
        </div>
    </div>
    <div style="width: 15px; height: 15px; left: 430px; top: 371px; position: absolute; background: #F25F5C; border-radius: 9999px"></div>
    <div style="width: 200px; height: 200px; left: 195px; top: 346px; position: absolute; background: rgba(100, 204, 197, 0.45); border-radius: 9999px; border: 4px #64CCC5 solid"></div>
</div>
</template>
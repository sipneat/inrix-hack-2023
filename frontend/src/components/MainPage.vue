<script>
    import GoogleMap from './googleMap.vue';
    import StreetView from './StreetView.vue';
</script>
<template>
    <link href='https://fonts.googleapis.com/css?family=Kanit' rel='stylesheet'>

    





    <div style="width: 100%; height: 100%; position: relative; background: #F60C0C">
    <div style="width: 100%; height: 135px; left: 0px; top: 0px; position: absolute; background: #053B50"></div>
    <div style="width: 360px; height: 811px; left: 920px; top: 184px; position: absolute; background: #176B87; border-radius: 15px"></div>
    <div style="width: 645px; height: 689px; left: 160px; top: 306px; position: absolute; background: #176B87; border-radius: 15px">
        <GoogleMap />
    </div>
    <div style="width: 486px; height: 101px; left: 477px; top: 17px; position: absolute; text-align: center; color: #EEEEEE; font-size: 70px; font-family: Kanit; font-weight: 600; line-height: 90px; word-wrap: break-word">Parking ++</div>
    <div style="width: 545px; padding-left: 8px; padding-right: 8px; left: 185px; top: 221px; position: absolute; background: white; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.16); border-radius: 24px; overflow: hidden; justify-content: flex-start; align-items: flex-start; gap: 8px; display: inline-flex; z-index: 1000">
        <img style="width: 40px; height: 40px" src="https://s3-alpha-sig.figma.com/img/2503/8781/6ba33e4e01d59ea6f3e0b1f4aa06d766?Expires=1700438400&Signature=iY6l3mOyKAhYSbcLxMxmYKUVTTzjT1x0B8H3mlbFgMxNOJa9GYnS8aNY4wBXe9oqZBE5fd5dEjqndWc8qxz4R5qLVp9k2UTIfOitWpQZ-8Lcw8NxfZ8Y2RgtmaAxF~kjAseLegrMHowquAvSivWFNMdGhKxGn3Ro0CwRkICPlSpqEA1yMxkyjHFE0ecVWGQl~tjUetyOtO-HdgP9VoaQwACJ6dGyL9g73GdSGTIqP9hUmRfPaX8vheZRZSP2uNgn5vZKTq9whyPUvdmj3VpbOdjxwdw68Oh6S~HwRANISKwSn2tJ8A2toq2qm9UBA7dG4jDX3Njr11-UQ5s~YvoS1w__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4" />
        <input class="search" type = "text" id = "location" location = "location" placeholder = "ex: Golden Gate Brg">
    </div>

    <div style="left: 735px; top: 215px; position: absolute">
        <button class="button2" type="submit">Submit</button>
    </div>
    
    
        
    

    <div style="width: 302px; height: 6px; left: 945px; top: 418px; position: absolute; background: #EEEEEE; border-radius: 100px">   </div>
    

    

    




    <div style="height: 436px; left: 952px; top: 488px; position: absolute; flex-direction: column; justify-content: flex-start; align-items: flex-start; gap: 55px; display: inline-flex">
        <div style="width: 288px; text-align: center; color: white; font-size: 32px; font-family: Kanit; font-weight: 600; line-height: 40px; word-wrap: break-word">Selected Parking:</div>
        <div style="justify-content: flex-start; align-items: center; gap: 15px; display: inline-flex">
            <div style="width: 53px; flex-direction: column; justify-content: flex-start; align-items: flex-end; gap: 55px; display: inline-flex">
                <div style="width: 45px; height: 45px; position: relative">
                    <img style="width: 40px; height: 40px" src="/Frame.png" />
                </div>
                <div style="width: 45px; height: 45px; position: relative; background: #176B87">
                    <img style="width: 40px; height: 40px" src="public\Frame1.png" />
                </div>
                <div style="width: 45px; height: 45px; position: relative">
                    <img style="width: 40px; height: 40px" src="public\Frame2.png" />
                </div>
            </div>
            <div style="flex-direction: column; justify-content: flex-start; align-items: flex-start; gap: 45px; display: inline-flex">
                <div style="width: 57px; height: 48px; padding: 10px; background: #F25F5C; border-radius: 15px; justify-content: center; align-items: center; gap: 10px; display: inline-flex">
                    <div style="text-align: center; color: #EEEEEE; font-size: 20px; font-family: Kanit; font-weight: 400; line-height: 20px; word-wrap: break-word">0</div>
                </div>
                <div style="width: 57px; height: 48px; padding: 10px; background: #F25F5C; border-radius: 15px; justify-content: center; align-items: center; gap: 10px; display: inline-flex">
                    <div style="text-align: center; color: #EEEEEE; font-size: 20px; font-family: Kanit; font-weight: 400; line-height: 20px; word-wrap: break-word">0</div>
                </div>
                <div style="width: 57px; height: 48px; padding: 10px; background: #F25F5C; border-radius: 15px; justify-content: center; align-items: center; gap: 10px; display: inline-flex">
                    <div style="text-align: center; color: #EEEEEE; font-size: 20px; font-family: Kanit; font-weight: 400; line-height: 20px; word-wrap: break-word">0</div>
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
            <!-- <div style="width: 67px; height: 48px; padding: 10px; background: #64CCC5; border-radius: 15px; justify-content: center; align-items: center; gap: 10px; display: flex">
                <div style="text-align: center; color: #EEEEEE; font-size: 20px; font-family: Kanit; font-weight: 400; line-height: 20px; word-wrap: break-word">0.2</div>
            </div>-->
            
            <button class="button1" type="submit">0.2</button>
            <!--<div style="width: 67px; height: 48px; padding: 10px; background: #64CCC5; border-radius: 15px; justify-content: center; align-items: center; gap: 10px; display: flex">
                <div style="text-align: center; color: #EEEEEE; font-size: 20px; font-family: Kanit; font-weight: 400; line-height: 20px; word-wrap: break-word">0.5</div>
            </div> -->
            <button class="button1" type="submit">0.5</button>
            <!-- <div style="width: 67px; height: 48px; padding: 10px; background: #64CCC5; border-radius: 15px; justify-content: center; align-items: center; gap: 10px; display: flex">
                <div style="text-align: center; color: #EEEEEE; font-size: 20px; font-family: Kanit; font-weight: 400; line-height: 20px; word-wrap: break-word">0.7</div>
            </div> --> 
            <button class="button1" type="submit">0.7</button>

           <!-- <div style="width: 67px; height: 48px; padding: 10px; background: #64CCC5; border-radius: 15px; justify-content: center; align-items: center; gap: 10px; display: flex">
                <div style="text-align: center; color: #EEEEEE; font-size: 20px; font-family: Kanit; font-weight: 400; line-height: 20px; word-wrap: break-word">1.0</div>
            </div> -->
            <button class="button1" type="submit">1.0</button>
        </div>
    </div>
</div>
</template>

<style scoped>



.main {
    width: 100%; 
    height: 100%; 
    padding-left: 8px; 
    padding-right: 8px; 
    background: white; 
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.16); 
    border-radius: 24px; 
    overflow: hidden; 
    justify-content: flex-start; 
    align-items: flex-start; 
    gap: 8px; 


    font-family: 'Kanit';
    font-size: 22px;





    display: inline-flex
}

.search {
    border: none; 
    width: 100%; 
    height: 100%; 
    opacity: 0.30; 
    color: black; 
    font-size: 30px; 
    font-family: Inter; 
    font-weight: 400; 
    word-wrap: break-word;
}

</style>
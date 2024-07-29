<template>
    <div class="upgrade">
        <div class="header">
            <h1 class="title">UPGRADE</h1>
        </div>

        <div class="blocks">
            <div class="block">
                <div class="photo">
                    <img class="spinner-one-fan" src="../assets/spinner-1-fan.png" alt="">
                </div>
                <div class="cost">
                    <p class="price">12 500</p>
                    <div class="logo-background">
                        <img class="logoSmall" src="../assets/logo-small.png" alt="">
                    </div>
                </div>
            </div>

            <div class="block">
                <div class="photo">
                    <img class="spinner-one-fan" src="../assets/spinner-1-fan.png" alt="">
                </div>
                <div class="cost">
                    <p class="price">12 500</p>
                    <div class="logo-background">
                        <img class="logoSmall" src="../assets/logo-small.png" alt="">
                    </div>
                </div>
            </div>

            <div class="block">
                <div class="photo">
                    <img class="spinner-one-fan" src="../assets/spinner-1-fan.png" alt="">
                </div>
                <div class="cost">
                    <p class="price">12 500</p>
                    <div class="logo-background">
                        <img class="logoSmall" src="../assets/logo-small.png" alt="">
                    </div>
                </div>
            </div>

            <div class="block">
                <div class="photo">
                    <img class="spinner-one-fan" src="../assets/spinner-1-fan.png" alt="">
                </div>
                <div class="cost">
                    <p class="price">12 500</p>
                    <div class="logo-background">
                        <img class="logoSmall" src="../assets/logo-small.png" alt="">
                    </div>
                </div>
            </div>
            
        </div>
    </div>
  
</template>

<script>
export default {

}
</script>

<style scoped>
.price{
    color: white;
    font-family: "Druk Wide";
    font-size: 12px;
    margin: 0;
    width: 70%;
}
.blocks{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(2, 1fr);
    grid-column-gap: 30px;
    grid-row-gap: 30px;
    padding: 0 30px;
}
.photo {
    background-color: #535453;
    border-radius: 10px;
    filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
}

.cost {
    background-color: #535453;
    border-radius: 10px;
    filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
    padding: 5px;
    display: flex;
    justify-content: space-between;
    margin-top: 5px;
    align-items: center;
}
.photo img{
    width: 100px;
}
.logo-background{
  width: 30px;
  height: 30px;
  background: linear-gradient(180deg, rgba(0,192,255,1) 0%, rgba(0,230,255,1) 100%);
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.logoSmall{
  width: 20px;
  height: 13px;
}
.header{
    width: 100%;
    height: 100px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.title{
    width: fit-content;
    padding: 5px 50px;
    height: 30px;
    background: linear-gradient(0deg, rgba(57,54,53,1) 0%, rgba(88,88,89,1) 100%);
    filter: drop-shadow(0 5px 5px rgb(23, 23, 23));
    color: white;
    font-family: "Druk Wide";
    font-size: 16px;
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 25px;
}
</style>
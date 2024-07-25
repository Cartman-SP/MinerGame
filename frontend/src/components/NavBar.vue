<template>
    <div class="nav">
        <button id="start" @click="changePage(1)">
            <svg width="34" height="34" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M17 3.4C9.48893 3.4 3.4 9.48893 3.4 17C3.4 24.5111 9.48893 30.6 17 30.6V34C7.61116 34 0 26.3888 0 17C0 7.61116 7.61116 0 17 0C26.3888 0 34 7.61116 34 17H30.6C30.6 9.48893 24.5111 3.4 17 3.4Z" :fill="getFillColor(1)"/>
            <path d="M20.4 22.8042L17 19.4042C16.3361 18.7403 16.3361 17.6639 17 17C17.6639 16.3361 18.7403 16.3361 19.4042 17L22.8042 20.4H30.6V23.8H26.2042L27.9042 25.5H34V28.9H31.3042L32.6521 30.2479L30.2479 32.6521L28.9 31.3042V34H25.5V27.9042L23.8 26.2042V30.6H20.4V22.8042Z" :fill="getFillColor(1)"/>
            <path d="M11.9 17C11.9 14.1833 14.1833 11.9 17 11.9C19.8167 11.9 22.1 14.1833 22.1 17H25.5C25.5 12.3056 21.6944 8.5 17 8.5C12.3056 8.5 8.5 12.3056 8.5 17C8.5 21.6944 12.3056 25.5 17 25.5V22.1C14.1833 22.1 11.9 19.8167 11.9 17Z" :fill="getFillColor(1)"/>
            </svg>
        </button>

        <button @click="changePage(2)">
            <svg width="34" height="34" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12.75 5.66667C12.75 2.53725 17.5072 0 23.375 0C29.2428 0 34 2.53725 34 5.66667C34 8.79608 29.2428 11.3333 23.375 11.3333C17.5072 11.3333 12.75 8.79608 12.75 5.66667ZM23.375 14.1667C21.9201 14.1667 20.5402 14.0038 19.2794 13.7204C17.3542 12.2768 14.1992 11.3333 10.625 11.3333C4.75717 11.3333 0 13.8706 0 17C0 20.1294 4.75717 22.6667 10.625 22.6667C16.4928 22.6667 21.25 20.1294 21.25 17C21.25 16.9589 21.2401 16.9192 21.2387 16.8782H21.25V19.8333C21.25 22.9627 16.4928 25.5 10.625 25.5C4.75717 25.5 0 22.9627 0 19.8333V22.6667C0 25.7961 4.75717 28.3333 10.625 28.3333C16.4928 28.3333 21.25 25.7961 21.25 22.6667V25.5C21.25 28.6294 16.4928 31.1667 10.625 31.1667C4.75717 31.1667 0 28.6294 0 25.5V28.3333C0 31.4627 4.75717 34 10.625 34C16.4928 34 21.25 31.4627 21.25 28.3333V28.22C21.9371 28.2937 22.6468 28.3333 23.375 28.3333C29.2428 28.3333 34 25.7961 34 22.6667V19.8333C34 22.8352 29.6197 25.2861 24.0833 25.4816V22.6483C29.6197 22.4528 34 20.0033 34 17V14.1667C34 17.1686 29.6197 19.6194 24.0833 19.8149V16.9816C29.6197 16.7861 34 14.3367 34 11.3333V8.5C34 11.6294 29.2428 14.1667 23.375 14.1667Z" :fill="getFillColor(2)"/>
            </svg>
        </button>

        <button @click="changePage(3)">
            <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 24H38V28H20V24Z" :fill="getFillColor(3)"/>
            <path d="M20 32H32V36H20V32Z" :fill="getFillColor(3)"/>
            <path d="M2 26C2 24.8954 2.89543 24 4 24H14C15.1046 24 16 24.8954 16 26V36C16 37.1046 15.1046 38 14 38H4C2.89543 38 2 37.1046 2 36V26Z" :fill="getFillColor(3)"/>
            <path d="M20 10H32V14H20V10Z" :fill="getFillColor(3)"/>
            <path d="M20 2H38V6H20V2Z" :fill="getFillColor(3)"/>
            <path d="M2 4C2 2.89543 2.89543 2 4 2H14C15.1046 2 16 2.89543 16 4V14C16 15.1046 15.1046 16 14 16H4C2.89543 16 2 15.1046 2 14V4Z" :fill="getFillColor(3)"/>
            </svg>
        </button>

        <button @click="changePage(4)">
            <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M28 8C28 12.4183 24.4183 16 20 16C15.5817 16 12 12.4183 12 8C12 3.58172 15.5817 0 20 0C24.4183 0 28 3.58172 28 8Z" :fill="getFillColor(4)"/>
            <path d="M2.00001 36C2.00004 29.3726 7.37261 24 14 24L26 24C32.6274 24 38 29.3726 38 36V38H2L2.00001 36Z" :fill="getFillColor(4)"/>
            </svg>
        </button>
    </div>
</template>

<script>
export default {
    data(){
        return{
            page: 2,
        }
    },
    methods:{
        changePage(id){
            this.page = id;
            switch (id) {
                case 1:
                    this.$router.push('loot');
                    break;
                case 2:
                    this.$router.push('clicker');
                    break;
                case 3:
                    this.$router.push('boosts');
                    break;
                case 4:
                    this.$router.push('model');
                    break;
            }
        },
        getFillColor(id) {
            if (id === this.page){
                return '#EB95F9'
            }else{
                return '#686D82'
            }
        }
    }
}
</script>

<style scoped>
.nav{
    margin: 15px 15px 30px 15px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    backdrop-filter: blur(10px);
    /* filter: drop-shadow(0 0 10px #df67f142); */
    border: 1px solid rgb(59, 59, 59);
    border-radius: 15px;
}

.nav svg{
    width: 20px;
    height: 20px;
    filter: drop-shadow(0 0 10px #df67f188);
}


#start{
    border-radius: 15px 0 0 15px;
}

#end{
    border-radius: 0 15px 15px 0;
}

.nav button{
    font-family: 'Montserrat';
    color: white;
    background-color: transparent;
    display: flex;
    border: none;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    padding: 15px;
}
</style>
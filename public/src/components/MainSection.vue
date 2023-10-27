<script>
    export default {}
</script>

<template>
    <div class="wrapper">
        <img src="/img/mainimg.png" alt="main-img">
        <div>
            <h1>Shop</h1>
            <h2>online</h2>
            <h3>now</h3>
            <p>Цены ниже на 50% только сегодня!</p>
            <button>Начать покупки</button>
        </div>
    </div>
</template>

<style scoped>
    .wrapper {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 150px 0;
    }

    .wrapper > div {
        margin-left: 300px;
    }

    .wrapper > div h1 {
        font-weight: 400;
        font-size: 90px;
    }

    .wrapper > div h2, .wrapper > div h3 {
        font-weight: 400;
        font-size: 70px;
    }

    .wrapper > div h3 {color: #97c7db;}

    .wrapper > div p {
        font-size: 18px;
        width: 500px;
        margin: 20px 0;
    }

    .wrapper > div button {
        font-weight: 600;
        font-size: 18px;
        color: #2F323A;
        background: #97c7db;
        border-radius: 25px;
        border: 0;
        padding: 15px 25px;
        cursor: pointer;
    }

    .wrapper > div button:hover {
        transform: translateY(-5px);
    }
</style>
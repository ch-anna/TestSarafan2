<script>
import Header from '../components/Header.vue'

export default {
  components: { Header }
}
</script>

<template>
<div class="wrapper">
    <div>
        <h1>Все товары</h1>
        <h2>Только самые лучшие товары для Вас</h2>
    </div>
    <div>
        <img src="/img/main.jpg" alt="">
    </div>
</div>
</template>

<style scoped>
.wrapper {
    background: #97c7db;
    width: 104%;
    position: relative;
    right: 13%;
    display: flex;
    padding: 0 12%;
    justify-content: space-between;
    align-items: center;
    height: 240px;
    color: #2F323A;
    margin: 60px 0;
}

.wrapper h1 {
    font-size: 70px;
}

.wrapper h2 {
    font-size: 30px;
    font-weight: 400;
    margin-top: 15px;
}

.wrapper img {
    height: 225px;
    border-radius: 20px;
}
</style>
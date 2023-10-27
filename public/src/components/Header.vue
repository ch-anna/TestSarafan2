<script>
export default {
    props: ['cart', 'clearCart'],
    data() {
        return {
            showCart: false
        }
    }
}
</script>

<template>
    <header>
        <img src="/img/logo.jpg" alt="logo">
        <ul>
            <li><RouterLink to="/" activ-class="active">Главная</RouterLink></li>
            <li><RouterLink to="/category" activ-class="active">Каталог</RouterLink></li>
            <li><RouterLink to="/delivery" activ-class="active">Доставка</RouterLink></li>
            <li><RouterLink to="/about" activ-class="active">О нас</RouterLink></li>
            <li><img src="/img/cart.jpg" alt="shopping-cart" @click="showCart = !showCart"></li>
        </ul>
        <div class="cart" v-if="showCart">
            <div class="box"></div>
            <h3 v-if="cart.length == 0">Корзина пуста</h3>
            <div class="items" v-else>
                <div class="item" v-for="el in cart" :key="el.slug">
                    <h3>{{ el.title }}</h3>
                    <span>{{ el.price }} &#8381</span>
                    <!-- <span> - {{ n }} шт </span> -->
                </div>
                <button @click="clearCart()">Очистить корзину</button>
            </div>
        </div>
    </header>
</template>

<style scoped>
    .cart {
        position: absolute;
        top: 45px;
        right: 0;
        padding: 20px;
        width: 250px;
        background: rgb(193, 66, 62);
        border-radius: 5px;
        z-index: 10;
        color: rgb(91, 31, 29);
    }

    .cart .box {
        background: rgb(193, 66, 62);
        position: absolute;
        top: -5px;
        right: 10px;
        width: 10px;
        height: 10px;
        transform: rotate(45deg);
    }

    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 30px;
        position: relative;
    }

    header ul {
        list-style: none;
    }

    header ul li {
        display: inline-block;
        margin-left: 25px;
        cursor: pointer;
    }

    header ul li .active {
        padding: 5px 15px;
        background: rgb(151 199 219);
        border-radius: 20px;
    }

    header ul li .active:hover {
        background: rgb(110, 144, 159);
        color: white;
    }

    header ul li a {
        position: relative;
        bottom: 8px;
    }
</style>
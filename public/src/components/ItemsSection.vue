<template>
    <div class="wrapper">
        <div v-for="el in sortedItems" :key="el.slug">
            <h3>{{ el.title }}</h3>
            <span>{{ el.price }} &#8381</span>
            <img src="/img/add-to-cart.png" alt="купить" @click="addtoCart(el)">
        </div>
    </div>
</template>

<script>

export default {
    props: ['addtoCart', 'sortedItems']
}
</script>

<style scoped>
img {width: 30px;}
</style>
<script>
import Header from '../components/Header.vue'
import HeadSection from  '../components/HeadSection.vue'
import ItemsSection from  '../components/ItemsSection.vue'

export default {
    props: ['cart', 'addtoCart', 'clearCart', 'sortedItems'],
    components: {Header, HeadSection, ItemsSection}
}
</script>

<template>
  <div>
    <Header :cart="cart" :clearCart="clearCart"/>
    <HeadSection />
    <ItemsSection :addtoCart="addtoCart" :sortedItems="sortedItems" />
  </div>
</template>

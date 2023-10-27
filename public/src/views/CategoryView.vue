<script>
import Header from '../components/Header.vue'
import HeadSection from  '../components/HeadSection.vue'
import CategorySection from  '../components/CategorySection.vue'

export default {
    props: ['cart', 'clearCart', 'sortItems'],
  components: {Header, HeadSection, CategorySection}
}
</script>

<template>
  <div>
    <Header :cart="cart" :clearCart="clearCart"/>
    <HeadSection />
    <CategorySection :sortItems="sortItems"/>
  </div>
</template>

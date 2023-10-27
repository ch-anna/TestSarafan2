<script>
import Header from '../components/Header.vue'
import MainSection from  '../components/MainSection.vue'

export default {
  props: ['cart', 'clearCart'],
  components: {Header, MainSection}
}
</script>

<template>
  <div>
    <Header :cart="cart" :clearCart="clearCart"/>
    <MainSection />
  </div>
</template>

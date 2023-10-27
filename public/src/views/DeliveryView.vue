<script>
import Header from '../components/Header.vue'
import DeliverySection from  '../components/DeliverySection.vue'

export default {
  props: ['cart', 'clearCart'],
  components: {Header, DeliverySection}
}
</script>

<template>
  <div>
    <Header :cart="cart" :clearCart="clearCart"/>
    <DeliverySection />
  </div>
</template>

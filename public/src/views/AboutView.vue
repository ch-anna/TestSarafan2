<script>
import Header from '../components/Header.vue'
import AboutSection from  '../components/AboutSection.vue'

export default {
  props: ['cart', 'clearCart'],
  components: {Header, AboutSection}
}
</script>

<template>
  <div>
    <Header :cart="cart" :clearCart="clearCart"/>
    <AboutSection />
  </div>
</template>

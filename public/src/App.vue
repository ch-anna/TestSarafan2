<script>
import { RouterView } from 'vue-router'
import axios from 'axios'

export default {
  data() {
    return{
      cart: [],
      items: [],
      sortedItems: []
    }
  },
  async mounted() {
        try {
            const items = await axios.get('http://localhost:8000/api/items/?format=json')
            this.items = items.data
        } catch(error) {
            console.log(error)
        }
    },
  methods: {
    addtoCart(item) {
      this.cart.push(item)
    },
    clearCart() {
      this.cart = []
      console.log('clear')
    },
    sortItems(subcat) {
      this.items.forEach(el => {
        if(el.subcategory == subcat) {
          this.sortedItems.push(el)
        }
      })
    }
  }
}
</script>

<template>
  <div class="container">
    <RouterView :cart="cart" :addtoCart="addtoCart" :clearCart="clearCart" :sortedItems="sortedItems" :sortItems="sortItems" />
  </div> 
</template>

<style scoped>

</style>

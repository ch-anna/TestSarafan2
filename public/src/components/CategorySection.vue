<template>
    <div class="wrapper">
        <div class="category" v-for="el in category" :key="el.slug">
            <h3>{{ el.title }}</h3>
            <div class="subcategory" v-for="el in subcategory" :key="el.slug">
                <a href="/items" @click="sortItems(el.id)">{{ el.title }}</a>
                <!-- <span @click="sortItems(el.id)">{{ el.title }}</span> -->
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    props: ['sortItems'],
    data() {
        return {
            category: [],
            subcategory: []
        }
    },
    async mounted() {
        try {
            const cat = await axios.get('http://localhost:8000/api/category/?format=json')
            // this.category = cat.data
            this.category = cat.data.results
            const subcat = await axios.get('http://localhost:8000/api/subcategory/?format=json')
            this.subcategory = subcat.data
        } catch(error) {
            console.log(error)
        }
    }
}
</script>

<style scoped>

</style>
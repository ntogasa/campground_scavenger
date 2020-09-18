const App = new Vue({
    el: '#show-camps',
    data() {
        return {
            campgrounds: [],
            search: '',
        };
    },
    async created() {
        const response = await fetch('http://localhost:8000/api/campgrounds/');
        this.campgrounds = await response.json();
    },
    methods: {
    },
    computed: {
        filteredCamps: function(){
            return this.campgrounds.filter((campground) => {
                return campground.parent.includes(this.search);
            });
        },
        filteredIDs: function(){
            return (this.filteredCamps.map(a => a.camp_id)).join(' ');
        },
    }
})
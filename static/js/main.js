const App = new Vue({
    el: '#show-camps',
    data() {
        return {
            campgrounds: [],
            search: '',
        };
    },
    async created() {
        const response = await fetch('https://campground-checker.herokuapp.com/api/campgrounds/');
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
        string_length: function(){
            return (this.search.length > 2);
        }
    }
})
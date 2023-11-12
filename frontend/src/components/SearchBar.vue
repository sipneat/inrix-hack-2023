<template>
    <div class="main">
        <img style="width: 40px; height: 40px" src="https://s3-alpha-sig.figma.com/img/2503/8781/6ba33e4e01d59ea6f3e0b1f4aa06d766?Expires=1700438400&Signature=iY6l3mOyKAhYSbcLxMxmYKUVTTzjT1x0B8H3mlbFgMxNOJa9GYnS8aNY4wBXe9oqZBE5fd5dEjqndWc8qxz4R5qLVp9k2UTIfOitWpQZ-8Lcw8NxfZ8Y2RgtmaAxF~kjAseLegrMHowquAvSivWFNMdGhKxGn3Ro0CwRkICPlSpqEA1yMxkyjHFE0ecVWGQl~tjUetyOtO-HdgP9VoaQwACJ6dGyL9g73GdSGTIqP9hUmRfPaX8vheZRZSP2uNgn5vZKTq9whyPUvdmj3VpbOdjxwdw68Oh6S~HwRANISKwSn2tJ8A2toq2qm9UBA7dG4jDX3Njr11-UQ5s~YvoS1w__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4" />
        <input class="search" type = "text" id = "location" location = "location" placeholder = "ex: Golden Gate Brg">
    </div>
</template>

<style scoped>

.main {
    width: 100%; 
    height: 100%; 
    padding-left: 8px; 
    padding-right: 8px; 
    background: white; 
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.16); 
    border-radius: 24px; 
    overflow: hidden; 
    justify-content: flex-start; 
    align-items: flex-start; 
    gap: 8px; 
    display: inline-flex
}

.search {
    border: none; 
    width: 100%; 
    height: 100%; 
    opacity: 0.30; 
    color: black; 
    font-size: 30px; 
    font-family: Inter; 
    font-weight: 400; 
    word-wrap: break-word;
}

</style>
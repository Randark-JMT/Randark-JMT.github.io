const ap = new APlayer({
    container: document.getElementById('aplayer'),
    fixed: true,
    autoplay: true,
    order: 'random',
    preload: 'auto',
    volume: 0.6,
    audio: [
        {
            name: '悠闲',
            artist: '沈以诚',
            url: '/music/mp3/悠闲-沈以诚.mp3',
            cover: '/music/cover/109951165711714155.jpg',
        },
        {
            name: "我可以",
            artist: '房东的猫',
            url: '/music/mp3/我可以-房东的猫.mp3',
            cover: '/music/cover/109951164475747593.jpg',
        },
        {
            name: "告白・告別",
            artist: 'nin',
            url: '/music/mp3/告白・告別-nin.mp3',
            cover: '/music/cover/109951165420802224.jpg',
        },
        {
            name: "夏日已所剩无几",
            artist: '泠鸢yousa',
            url: '/music/mp3/夏日已所剩无几-泠鸢yousa.mp3',
            cover: '/music/cover/109951162817808719.jpg',
        },
        {
            name: "关于风起时",
            artist: '唐映枫',
            url: '/music/mp3/关于风起时-唐映枫.mp3',
            cover: '/music/cover/109951163243210206.jpg',
        }
    ]
});
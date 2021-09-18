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
            url: 'http://music.163.com/song/media/outer/url?id=1819028025.mp3',
            cover: 'http://p2.music.126.net/0VtSwJd9WGzyYg6zjAbtAQ==/109951165711714155.jpg',
        },
        {
            name: "我可以",
            artist: '房东的猫',
            url: 'http://music.163.com/song/media/outer/url?id=1401909095.mp3',
            cover: 'http://p2.music.126.net/61775q0TRq4owulLLXi58Q==/109951164475747593.jpg',
        },
        {
            name: "告白・告別",
            artist: 'nin',
            url: 'http://music.163.com/song/media/outer/url?id=1491007768.mp3',
            cover: 'http://p2.music.126.net/Ag8qI5yNsB_qv7x9yzqjZQ==/109951165420802224.jpg',
        },
        {
            name: "夏日已所剩无几",
            artist: '泠鸢yousa',
            url: 'http://music.163.com/song/media/outer/url?id=444706525.mp3',
            cover: 'http://p1.music.126.net/GULe52JbCtVW0vjXZ1o2yw==/109951162817808719.jpg',
        },
        {
            name: "关于风起时",
            artist: '唐映枫',
            url: 'http://music.163.com/song/media/outer/url?id=514052896.mp3',
            cover: 'http://p2.music.126.net/guXPSjJahn5RwMwMES4crw==/109951163243210206.jpg',
        }
    ]
});
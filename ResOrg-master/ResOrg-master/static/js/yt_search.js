let nextPageToken = '';
let prevPageToken = '';

async function searchYouTube(query, pageToken = '') {
    const apiKey = 'AIzaSyA5Hgs0_AZpLs8uzPW7dNAi3BAupl01v6U';
    const url = `https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q=${query}&key=${apiKey}&pageToken=${pageToken}`;

    try {
        const response = await fetch(url);
        const data = await response.json();
        const videoIds = data.items.map(item => item.id.videoId).join(',');
        const detailsUrl = `https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id=${videoIds}&key=${apiKey}`;
        const detailsResponse = await fetch(detailsUrl);
        const detailsData = await detailsResponse.json();
        displayResults(detailsData.items);
        nextPageToken = data.nextPageToken || '';
        prevPageToken = data.prevPageToken || '';
        updatePaginationButtons();
    } catch (error) {
        console.error('Error fetching YouTube data:', error);
    }
}

async function getChannelIcon(channelId) {
    const apiKey = 'AIzaSyA5Hgs0_AZpLs8uzPW7dNAi3BAupl01v6U';
    const url = `https://www.googleapis.com/youtube/v3/channels?part=snippet&id=${channelId}&key=${apiKey}`;

    try {
        const response = await fetch(url);
        const data = await response.json();
        return data.items[0].snippet.thumbnails.default.url;
    } catch (error) {
        console.error('Error fetching channel icon:', error);
        return '';
    }
}

async function displayResults(videos) {
    const resultsDiv = document.getElementById('yt-results');
    resultsDiv.innerHTML = '';

    for (const video of videos) {
        const videoId = video.id;
        const title = video.snippet.title;
        const description = video.snippet.description;
        const channelTitle = video.snippet.channelTitle;
        const publishedAt = new Date(video.snippet.publishedAt).toLocaleDateString();
        const viewCount = video.statistics.viewCount;
        const channelId = video.snippet.channelId;
        const channelIcon = await getChannelIcon(channelId);

        const videoElement = document.createElement('div');
        videoElement.classList.add('yt-search-card');
        videoElement.innerHTML = `
            <div class="yt-card-video">
                <iframe class="item-ytplayer" width="350" height="200" src="https://www.youtube.com/embed/${videoId}" frameborder="0" allow="encrypted-media; autoplay; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin">
                </iframe>
            </div>
            <div class="yt-card-info">
                <div class="yt-card-info-title">${title}</div>
                <div class="yt-card-info-stats">${viewCount} views <span class="yt-card-info-stats-period">•</span> ${publishedAt}</div>
                <div class="yt-card-info-channel">
                    <div><img class="yt-card-info-channel-profile" src="${channelIcon}"></div>
                    <div class="yt-card-info-channel-name">${channelTitle}</div>
                </div>
                <div class="yt-card-info-desc">${description}</div>
                <div class="yt-card-info-interaction"> 
                    <button class="yt-card-info-button"><img class="yt-card-info-button-icon" src="{% static 'media/plus.png' %}">Add to Topic</button>
                </div>
            </div>
        `;
        resultsDiv.appendChild(videoElement);
    }
}

function updatePaginationButtons() {
    document.getElementById('yt-result-prev-button').disabled = !prevPageToken;
    document.getElementById('yt-result-next-button').disabled = !nextPageToken;
}

function handleSearch() {
    const query = document.getElementById('query').value;
    if( query.length == 0 ) return;
    document.getElementById('yt-result-container').style.display = "block";
    searchYouTube(query);
}

function handleNextPage() {
    const query = document.getElementById('query').value;
    searchYouTube(query, nextPageToken);
}

function handlePrevPage() {
    const query = document.getElementById('query').value;
    searchYouTube(query, prevPageToken);
}

function closeYTResultContainer(){
    document.getElementById('yt-result-container').style.display = "none";
    document.getElementById('query').value = "";
}

function enterQuery(event){
    if (event.key == "Enter") {
        handleSearch();
    }
}
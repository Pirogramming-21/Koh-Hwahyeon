const chatInput=document.getElementById('chat-input');
const hashtagBtn =document.getElementById('hashtag');
const sendBtn=document.getElementById('btn-send');


chatInput.focus();

chatInput.addEventListener('input', (event)=> {
    if(event.target.value =='') {
        hashtagBtn.style.display='block';
        sendBtn.style.display='none';
    }
    else {
        hashtagBtn.style.display='none';
        sendBtn.style.display='block';
    }
});

chatInput.addEventListener('keypress', (event) => {
    if(event.code=='Enter') {
        sendBtn.click();
    }
});

let flag=true;

const chatBubbleContainer = document.getElementById('chat-bubble');

sendBtn.addEventListener('click', ()=> {
    const contentDiv=document.createElement('div');

    if(flag) {
        contentDiv.className='my-bubble-content';

        const bubble=document.createElement('div');
        bubble.className='my-bubble';

        bubble.innerText=chatInput.value;
        contentDiv.appendChild(bubble);

        flag=false;
    }
    else {
        contentDiv.className='your-bubble';
        const profileDiv=document.createElement('div');
        profileDiv.className='profile';

        const profileImg=document.createElement('img');
        profileImg.src='./profile.png';

        profileDiv.appendChild(profileImg);
        contentDiv.appendChild(profileDiv);

        const bubbleContent=document.createElement('div');
        bubbleContent.className='bubble-content';

        const name=document.createElement('div');
        name.className='name';
        name.innerText='교육팀장님';

        const bubble=document.createElement('div');
        bubble.className='bubble';
        bubble.innerText=chatInput.value;

        bubbleContent.appendChild(name);
        bubbleContent.append(bubble);

        contentDiv.appendChild(bubbleContent);

        flag=true;
    }

    chatBubbleContainer.appendChild(contentDiv);

    chatBubbleContainer.scrollTop=chatBubbleContainer.scrollHeight;

    hashtagBtn.style.display='block';
    sendBtn.style.display='none';

    chatInput.value='';
});
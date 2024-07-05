let seconds =0;
let millis=0;

const second=document.getElementById('second');
const milli=document.getElementById('milli');
const startBtn=document.getElementById('start');
const stopBtn=document.getElementById('stop');
const resetBtn=document.getElementById('reset');

startBtn.addEventListener('click', ()=>{
    interval=setInterval(()=>{
        millis++;
        if(millis<10) {
            milli.innerText='0'+millis;
        }
        else {
            milli.innerText=millis;
        }
        if (millis>99)
        {
            seconds++;
            if(seconds<10) {
                second.innerText='0'+seconds;
            }
            else {
                second.innerText=seconds;
            }
            millis=0;
            milli.innerText='00';
        }
    }, 10)
})
/*<div class="record-box">
            <div class="record-head">
                <i class="ri-circle-line"></i>
                <sapn class="record-head-text">구간 기록</sapn>
                <i class="ri-delete-bin-fill"></i>
            </div>
            <div class="record-content">
                <div class="record">
                </div>
            </div>
        </div>*/


stopBtn.addEventListener('click',()=>{
    clearInterval(interval);

    const recordContent = document.querySelector('.record-content');
    const recordline=document.createElement('div');
    const record = document.createElement('span');
    const icon=document.createElement('i');

    recordline.className='record-line';
    record.className = 'record';
    icon.className='ri-circle-line';

    record.style.width='36vh';
    recordContent.style.height='8vh';
    let text='';

    if(seconds<10) {
        text+='0'+seconds;
    }
    else {
        text+=seconds;
    }
    if(millis<10) {
        text+=':'+'0'+millis;
    }
    else {
        text+=':'+millis;
    }

    record.innerText=text;
    recordline.appendChild(icon);
    recordline.appendChild(record);
    recordContent.appendChild(recordline);

    const trash=document.querySelector('.ri-delete-bin-fill');
    const head_icon=document.getElementById('head-ri-circle-line');

    icon.addEventListener('click', ()=>{
        icon.classList.toggle('ri-circle-line');
        icon.classList.toggle('ri-checkbox-circle-line');

        const icons = document.querySelectorAll('.ri-circle-line, .ri-checkbox-circle-line');
        let all = true;
    
        for(let i=0; i<icons.length;i++) {
            if(icons[i].className!='ri-checkbox-circle-line') {
                all=false;
                break;
            }
        }
    
        if (all==true) {
            head_icon.classList.remove('ri-circle-line');
            head_icon.classList.add('ri-checkbox-circle-line');
        } 
        else {
            head_icon.classList.remove('ri-checkbox-circle-line');
            head_icon.classList.add('ri-circle-line');
        }
    })

    head_icon.addEventListener('click', () => {
        head_icon.classList.toggle('ri-circle-line');
        head_icon.classList.toggle('ri-checkbox-circle-line');
        const icons = document.querySelectorAll('.ri-circle-line, .ri-checkbox-circle-line');

        for (let i = 0; i < icons.length; i++) {
            if (head_icon.classList.contains('ri-circle-line')) {
                icons[i].className = 'ri-circle-line';
            } 
            else {
                icons[i].className = 'ri-checkbox-circle-line';
            }
        }
    })

    
    trash.addEventListener('click', ()=>{
        if(icon.className=='ri-checkbox-circle-line') {
            recordline.style.display='none';
        } 
    });
});

resetBtn.addEventListener('click',()=>{
    clearInterval(interval);
    second.innerText='00';
    milli.innerText='00';
    millis=0;
    seconds=0;
})

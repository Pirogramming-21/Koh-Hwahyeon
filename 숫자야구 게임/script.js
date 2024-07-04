let chance=9;
const answer_list=new Array(3);
let result_img=document.getElementById('game-result-img');

document.addEventListener('DOMContentLoaded', function reset() {

    for (let i=0;i<3;i++) {
        answer_list[i]=Math.floor(Math.random()*10);
        if (answer_list[i]==answer_list[i-1] ||answer_list[i]==answer_list[i-2])
            i--;
    }

    const result=document.querySelector('.result-display');
    result.innerHTML='';
    const inputs=document.querySelectorAll('.input-field');
    for(let i=0;i<3;i++)
    {
        inputs[i].value='';
    }
    result_img.src='';

})

/* <div class="result-display">  
    <div class="check-result">
        <div class="left">3 5 6</div>
        :
        <div class="right">
            1 <div class="strike num-result">S</div>
            1 <div class="ball num-result">B</div>
        </div>
    </div>*/

function check_numbers() {
    const inputs=document.getElementsByClassName('input-field');
    const result=document.querySelector('.result-display');
    const check_result=document.createElement('div');
    const result_left=document.createElement('div');
    const result_right=document.createElement('div');
    const right_strike_result=document.createElement('div');
    const right_ball_result=document.createElement('div');
    const right_out_result=document.createElement('div');
    
    check_result.className = 'check-result';
    result_left.className = 'left';
    result_right.className = 'result';
    right_strike_result.className = 'strike num-result';
    right_ball_result.className = 'ball num-result';
    right_out_result.className = 'out num-result';
    
    const userNumbers = [
        parseInt(inputs[0].value),
        parseInt(inputs[1].value),
        parseInt(inputs[2].value)
    ];

    
    result_left.innerText=userNumbers.join(' ');

    let strike = 0;
    let ball = 0;

    for (let i = 0; i < 3; i++) {
        if (userNumbers[i]=='') {
            for(let i=0;i<3;i++)
                {
                    inputs[i].value='';
                }
            break;
        }
        else {
            if (userNumbers[i] == answer_list[i]) {
                strike++;
            } 
            else {
                for (let j = 0; j < 3; j++) {
                    if (userNumbers[i] == answer_list[j]) {
                        ball++;
                        break;
                    }
                }
            }
        }
    }

    /*display: inline;
    padding: 8px;
    border-radius: 50%;*/

    right_strike_result.style.display='inline';
    right_ball_result.style.display='inline';
    right_strike_result.innerText = `:      S-${strike}`;
    right_ball_result.innerText = `:        B-${ball}`;

    if(strike==0 && ball==0) {
        right_out_result.innerText='O';
        right_strike_result.style.display='none';
        right_ball_result.style.display='none';
    }
    else{
        right_out_result.style.display='none';
    }

    result.appendChild(check_result);
    check_result.appendChild(result_left);
    check_result.appendChild(result_right);
    result_right.appendChild(right_strike_result);
    result_right.appendChild(right_ball_result);
    result_right.appendChild(right_out_result);

    chance--;

    const button=document.querySelector('.submit-button');
    button.style.border='2px solid black';

    if(chance==0 &&strike!=3) {
        result_img.src='./fail.png'
        button.style.border='none';
        }
    else if(chance>0 && strike==3) {
        result_img.src='./success.png';
        button.style.border='none';
    }
}


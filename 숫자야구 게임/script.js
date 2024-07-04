const answer_list=new Array(3);
for (let i=0;i<3;i++) {
    answer_list[i]=Math.floor(Math.random()*10);
    if (answer_list[i]==answer_list[i-1] ||answer_list[i]==answer_list[i-2])
        i--;
}
/* <div class="result-display">  
    <div class="check-result">
        <div class="left">3 5 6</div>
        :
        <div class="right">
            1 <div class="strike num-result">S</div>
            1 <div class="ball num-result">B</div>
        </div>
    </div>*/
let chance=9;
function check_numbers() {
    const inputs=document.getElementsByClassName('input-field');
    const box_container=document.querySelector('.result-display');
    const check_box=document.createElement('div');
    const box_left=document.createElement('div');
    const box_right=document.createElement('div');
    const right_strike_result=document.createElement('div');
    const right_ball_result=document.createElement('div');
    const right_out_result=document.createElement('div');

    check_box.className = 'check-result';
    box_left.className = 'left';
    box_right.className = 'right';
    right_strike_result.className = 'strike num-result';
    right_ball_result.className = 'ball num-result';
    right_out_result.className = 'out num-result';
    
    const userNumbers = [
        parseInt(inputs[0].value),
        parseInt(inputs[1].value),
        parseInt(inputs[2].value)
    ];

    box_left.innerText=userNumbers.join(' ');

    let strike = 0;
    let ball = 0;

    for (let i = 0; i < 3; i++) {
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

    right_strike_result.innerText=strike+'';
    right_ball_result.innerText=ball;

    if(strike==0 && ball==0) {
        right_out_result.innerText='o';
    }

    box_container.appendChild(check_box);
    check_box.appendChild(box_left);
    check_box.appendChild(box_right);
    box_right.appendChild(right_strike_result);
    box_right.appendChild(right_ball_result);
    box_right.appendChild(right_out_result);

    chance--;

    if(chance==0 &&strike!=3)
        {
            const result = document.getElementById('game-result-img');
            result.src = './fail.png';
        }
    else {
        result.src='./success.png';
    }
}


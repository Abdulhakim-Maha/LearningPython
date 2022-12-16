function solution(str) {
  ls = [];
  while (str.length >= 1) {
    if (str.length === 1) {
      ls.push(str.slice(0, 1) + "_");
      str = str.slice(1);
    } else {
      ls.push(str.slice(0, 2));
      str = str.slice(2);
    }
  }
//   console.log(ls, str);
  return ls
}

solution("austini");

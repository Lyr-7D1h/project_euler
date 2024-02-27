// const LIMIT: u32 = 24;
const LIMIT: u32 = 28123;

fn main() {
    let mut abundant: Vec<u32> = vec![];
    let mut sum = 0;
    'outer: for x in 1..=LIMIT {
        let mut divisors = 0;
        // TODO: implement efficient aliquot sum https://math.stackexchange.com/questions/4484414/what-are-the-most-efficient-ways-to-calculate-the-sum-of-positive-divisors-funct
        for i in 1..=x / 2 {
            if x % i == 0 {
                divisors += i;
                if divisors > x {
                    abundant.push(x);
                    break;
                }
            }
        }

        for i in abundant.iter() {
            for j in abundant.iter() {
                if i + j > 28123 {
                    break;
                }
                if i + j == x {
                    continue 'outer;
                }
            }
        }

        sum += x;
    }

    println!("{sum}");
}

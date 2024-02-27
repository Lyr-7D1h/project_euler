fn fact(x: usize) -> usize {
    (1..=x).into_iter().product()
}

fn main() {
    let mut t = 1000000;

    let mut perm = [None; 10];

    for i in (0..=9).rev() {
        let f = fact(i);
        let p = t / f;
        t -= p * f;

        if t == 0 && i > 0 {
            let mut i = 0;
            for p in perm.iter_mut() {
                if p.is_none() {
                    *p = Some(i);
                    i += 1;
                }
            }
        }

        let mut index = i - p;
        for j in 0..perm.len() {
            if perm[j].is_some() {
                continue;
            }
            if index == 0 {
                println!("{j} {t}");
                perm[j] = Some(i);
                break;
            }
            index -= 1;
        }
    }

    println!(
        "{}",
        perm.into_iter()
            .map(|x| x.unwrap().to_string())
            .collect::<Vec<String>>()
            .join("")
    );
}

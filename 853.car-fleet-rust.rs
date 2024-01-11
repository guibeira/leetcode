// @leet start
impl Solution {
    pub fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
        let target = target as f64;
        let mut pairs = Vec::new();
        let mut fleets = 0;
        let mut curtime = 0.0;

        for i in 0..position.len() {
            let p = (position[i], speed[i]);
            pairs.push(p);
        }

        //println!("{:?}", pairs);
        pairs.sort();

        for p in pairs.iter().rev() {
            let destination_time = (target - p.0 as f64) / p.1 as f64;
            // println!(
            //     "position={} speed={} destination={:?} curtime={}",
            //     p.0, p.1, destination_time, curtime
            // );
            if curtime < destination_time {
                fleets += 1;
                curtime = destination_time;
            }
        }
        fleets
    }
}
// @leet end
